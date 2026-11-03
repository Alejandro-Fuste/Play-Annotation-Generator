# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_59`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_59/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 69 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [20-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-59] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-65] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-183] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [80-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-65] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-70] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-28] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [31-96] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-82] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-106] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-124] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-187] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [157-182] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-195] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.