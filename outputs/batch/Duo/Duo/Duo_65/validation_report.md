# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_65`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_65/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 53 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-179] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-179] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-179] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-174] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-163] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [115-142] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-147] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-152] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-136] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [151-152] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-179] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-144] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-168] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-177] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-160] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [156-157] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [175-179] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-157] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-179] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-171] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [177-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-179] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [97-111] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-177] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [122-127] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [165-179] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-179] for track '22' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.