# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_191`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_191/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 20 |
| Ball Tracks | 1 |
| CSV events parsed | 13 |
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
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [79-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [103-118] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-100] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [112-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-96] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [98-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-99] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-120] for track '20' has 1 frames without a visible bounding box.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.