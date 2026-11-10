# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_183`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_183/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 19 |
| Player Tracks | 18 |
| Ball Tracks | 1 |
| CSV events parsed | 9 |
| Action Segments inferred | 27 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 368: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-120] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-76] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-107] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-120] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' for track '4' starts at frame 71, but the player has no visible bounding box on this frame.
> - Action 'Action_CloseOnQuarterback' range [71-95] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [114-120] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-71] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-120] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-36] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-41] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-120] for track '13' has 6 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-120] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-120] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-107] for track '18' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.