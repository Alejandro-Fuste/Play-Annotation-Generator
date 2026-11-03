# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_28`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_28/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 54 |
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
> - Action 'Action_PreSnap' range [0-159] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [53-214] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-24] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BlockPunt' range [67-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-86] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-175] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-88] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [92-108] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-112] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-121] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-108] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-136] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-148] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-159] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-167] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-189] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-207] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [208-213] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-239] for track '35' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.