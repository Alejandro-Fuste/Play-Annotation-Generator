# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_131`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_131/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 56 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [152-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-166] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [172-175] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [162-164] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [81-129] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-179] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [163-172] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-128] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-100] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-145] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-157] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-172] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-121] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [123-125] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-179] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-126] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [80-117] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [119-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-165] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-87] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [96-97] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [100-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-118] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-179] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '24' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.