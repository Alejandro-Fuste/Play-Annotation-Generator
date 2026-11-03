# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_30`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [5-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-197] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [64-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [180-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [184-185] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [216-220] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [223-253] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-21] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-212] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [214-217] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-128] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-167] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-135] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-250] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-299] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-76] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-275] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [278-285] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-296] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-65] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-168] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-205] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-122] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-168] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-26] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-173] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-299] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [5-162] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [5-56] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-141] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-299] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [34-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-44] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-197] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-103] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [105-276] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-158] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [120-133] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [150-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-216] for track '27' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-253] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-286] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-230] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-238] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-257] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-290] for track '32' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [289-299] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-297] for track '37' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.