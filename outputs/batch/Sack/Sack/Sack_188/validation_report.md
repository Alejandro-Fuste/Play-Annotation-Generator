# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_188`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_188/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 39 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-180] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-180] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-104] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [151-156] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [170-173] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-129] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [131-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-95] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-180] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-180] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-159] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [161-162] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-147] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-180] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-122] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-140] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [119-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [160-161] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-179] for track '22' has 1 frames without a visible bounding box.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.