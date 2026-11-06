# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntCoverage_9`
- **Input XML**: `outputs/batch/PuntCoverage/PuntCoverage/PuntCoverage_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntCoverage.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 41 |
| Player Tracks | 41 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 19: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [17-169] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-185] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-223] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-260] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-292] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-47] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-187] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-44] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [50-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-164] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-78] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-154] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-187] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-190] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-205] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-215] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-59] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-66] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_Tackle' range [211-240] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-56] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-226] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-198] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [200-205] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-219] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [17-266] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-299] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-296] for track '15' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [17-86] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-229] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-282] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_LongSnap' range [17-71] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [72-289] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-299] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-35] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [44-239] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-255] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [40-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-68] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [74-75] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-86] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [69-299] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [98-295] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-191] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-216] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-242] for track '28' has 7 frames without a visible bounding box.
> - Action 'Action_None' range [247-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [116-118] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-147] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-157] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-294] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-233] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-247] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [214-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-299] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-299] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-291] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '40' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.