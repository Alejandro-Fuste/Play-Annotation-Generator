# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_120`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 18 |
| Player Tracks | 18 |
| Ball Tracks | 0 |
| CSV events parsed | 8 |
| Action Segments inferred | 38 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 242: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 242: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-113] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [114-149] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-89] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-93] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-138] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-117] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-41] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-55] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-80] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-92] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-66] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-45] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-127] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [54-60] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-55] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [52-80] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [91-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [119-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [130-150] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-89] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-128] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-135] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-81] for track '17' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.