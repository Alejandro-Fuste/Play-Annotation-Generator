# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_105`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_105/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 151 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [23-65] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-269] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [23-245] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-74] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-169] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-184] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-222] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-122] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-161] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-225] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-245] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-258] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-41] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-77] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-97] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-228] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-40] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-70] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-38] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [49-52] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-72] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-97] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-116] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-123] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-164] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-269] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [36-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-57] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-99] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-182] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-32] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [24-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-93] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-109] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-128] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-154] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-166] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-131] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-185] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-147] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-227] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [137-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-182] for track '30' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [215-225] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-143] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-173] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-190] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [196-212] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-217] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-257] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-212] for track '34' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [214-245] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-269] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-219] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-246] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-239] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-226] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-244] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-246] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '42' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.