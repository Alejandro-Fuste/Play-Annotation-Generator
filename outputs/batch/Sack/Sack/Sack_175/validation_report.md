# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_175`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_175/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 22 |
| Player Tracks | 21 |
| Ball Tracks | 1 |
| CSV events parsed | 9 |
| Action Segments inferred | 40 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 352: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-27] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-93] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [32-96] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-135] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-97] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [113-150] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-23] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-67] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [6-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-113] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [62-143] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [100-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [102-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-150] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [122-124] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [127-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [133-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [137-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [141-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [146-147] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [137-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-150] for track '21' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.