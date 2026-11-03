# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_21`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 51 |
| Player Tracks | 51 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 44: Duplicate assignment for track ID '3' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [33-66] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-240] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-214] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-97] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-230] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-284] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [88-230] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [233-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-70] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-59] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-63] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [33-52] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-183] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [187-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-97] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-151] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-163] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-237] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [33-242] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-101] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-224] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-213] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [33-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-295] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-70] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-95] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [97-244] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-132] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-138] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-141] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-176] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-291] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [139-141] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-143] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-146] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-166] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [176-187] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-230] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-260] for track '31' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [263-274] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-261] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-192] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-201] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-192] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-218] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-285] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [195-229] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-202] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-256] for track '42' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [259-262] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-247] for track '43' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-287] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-282] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [285-288] for track '46' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-299] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-298] for track '49' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '46' has undefined position. Will map to Position_Unknown.
> - Player track '46' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.
> - Player track '49' has undefined position. Will map to Position_Unknown.
> - Player track '49' has undefined team_side. Will map to Team_Unknown.
> - Player track '50' has undefined position. Will map to Position_Unknown.
> - Player track '50' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.