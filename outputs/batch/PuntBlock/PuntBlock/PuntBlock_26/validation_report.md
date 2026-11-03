# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_26`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_26/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
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
> - Action 'Action_None' range [1-45] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-53] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-62] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-69] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-49] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-210] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-53] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-57] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-67] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-159] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [52-180] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-117] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-109] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-194] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-163] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-210] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-55] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-133] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [138-143] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-148] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-112] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-24] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-128] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-210] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-181] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-148] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-210] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '29' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.