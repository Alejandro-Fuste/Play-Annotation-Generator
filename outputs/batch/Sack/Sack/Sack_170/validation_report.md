# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_170`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_170/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 22 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 30 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [90-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [101-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [93-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-111] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-116] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '21' has 1 frames without a visible bounding box.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.