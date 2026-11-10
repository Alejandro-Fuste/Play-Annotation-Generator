# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_155`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_155/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 17 |
| Player Tracks | 16 |
| Ball Tracks | 1 |
| CSV events parsed | 9 |
| Action Segments inferred | 29 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 312: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-74] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-81] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [82-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [97-98] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [101-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [108-112] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [115-117] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' for track '3' starts at frame 120, but the player has no visible bounding box on this frame.
> - Action 'Action_SackQuarterback' range [120-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-102] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-33] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-120] for track '16' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.