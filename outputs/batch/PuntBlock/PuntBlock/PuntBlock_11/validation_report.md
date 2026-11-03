# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_11`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_11/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
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
> - Action 'Action_PreSnap' range [0-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [55-67] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [83-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PuntBall' range [50-172] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-90] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-139] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-189] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-88] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-124] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-25] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-108] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-218] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-36] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-67] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-232] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-91] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-115] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [128-129] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-138] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [225-234] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-228] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-181] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-205] for track '28' has 1 frames without a visible bounding box.
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