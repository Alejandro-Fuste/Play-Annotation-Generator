# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_29`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 5 |
| Action Segments inferred | 71 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 60: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 60: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 60: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 60: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-155] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PlaceBall' range [28-49] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-153] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-105] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-166] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-55] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-115] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [118-210] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-42] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-68] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-70] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-33] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-48] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [51-77] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-23] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [68-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-87] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [99-101] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-160] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-60] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [90-93] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [97-101] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-121] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-198] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-37] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-119] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-27] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [31-32] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [46-47] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-85] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-87] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [117-138] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-153] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-210] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-134] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-134] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-150] for track '29' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-178] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [150-210] for track '31' has 1 frames without a visible bounding box.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.