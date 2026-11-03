# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `OutRoutes_3`
- **Input XML**: `outputs/batch/OutRoutes/OutRoutes/OutRoutes_3/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutRoutes.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 66 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Row 5, Column 'Pass Block': Could not parse frame number from '-' in entry '-,OL'.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 7: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 8: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_BallCarry' range [89-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-98] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-58] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-137] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-107] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-113] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-100] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [15-150] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-18] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-111] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-25] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-109] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-32] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-38] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [45-48] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-52] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-60] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-65] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-77] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-81] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-97] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-107] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-115] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-34] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-49] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [110-115] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-150] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-110] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [72-107] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-85] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [86-90] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-101] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-139] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-138] for track '34' has 1 frames without a visible bounding box.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.