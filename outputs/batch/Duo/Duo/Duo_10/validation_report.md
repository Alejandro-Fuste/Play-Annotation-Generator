# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_10`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 26 |
| Ball Tracks | 2 |
| CSV events parsed | 18 |
| Action Segments inferred | 51 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-135] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-118] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [122-141] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-179] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [140-179] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [93-99] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [106-107] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [116-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-154] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [156-160] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-179] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [93-130] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-128] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-132] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-179] for track '20' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-31] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-67] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [138-179] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-143] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-149] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [153-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-162] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [178-179] for track '27' has 1 frames without a visible bounding box.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.