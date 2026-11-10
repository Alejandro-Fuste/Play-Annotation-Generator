# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_117`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 236: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 236: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-95] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [120-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-95] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-131] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [133-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-142] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-90] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-150] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-111] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-122] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [125-150] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [114-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [130-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '26' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.