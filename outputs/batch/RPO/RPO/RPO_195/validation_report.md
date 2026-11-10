# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_195`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_195/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 45 |
| Player Tracks | 45 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 153 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 360: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_None' range [98-216] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-389] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-126] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-160] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-254] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-263] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-145] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [149-190] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-254] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-349] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-116] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-138] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-262] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [265-330] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-159] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-193] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-357] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-116] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-119] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-343] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-194] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [108-123] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBall' range [124-128] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [132-133] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 159, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [159-264] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-129] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-224] for track '15' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [226-328] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-117] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-234] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-170] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-177] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-218] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-354] for track '17' has 7 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-200] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [221-250] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [99-127] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-153] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-187] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-255] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [98-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-182] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-166] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-273] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-186] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-272] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-282] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-179] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-279] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [200-231] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [234-241] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-265] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-272] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-282] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-294] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-308] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-316] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-318] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-292] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-292] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-324] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-317] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-339] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-360] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [359-370] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [363-364] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [366-368] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [371-389] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [387-389] for track '43' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.