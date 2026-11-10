# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_68`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_68/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 17 |
| Player Tracks | 16 |
| Ball Tracks | 1 |
| CSV events parsed | 10 |
| Action Segments inferred | 27 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_CloseOnQuarterback' range [92-94] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [117-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-115] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-91] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [108-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-80] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [110-117] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-120] for track '16' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.