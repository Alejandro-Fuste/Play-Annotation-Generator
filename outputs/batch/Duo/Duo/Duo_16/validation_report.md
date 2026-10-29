# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_16`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_16/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 24 |
| Ball Tracks | 1 |
| CSV events parsed | 15 |
| Action Segments inferred | 70 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 33: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 34: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-91] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [103-106] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [109-110] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [144-149] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [60-87] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-99] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-45] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-53] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-62] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-69] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-69] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [47-52] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [57-59] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [61-79] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-112] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-129] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [47-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-102] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-149] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-127] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-136] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [139-148] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-101] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-119] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-139] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [143-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-101] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-111] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-78] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-149] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-64] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-76] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [47-66] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-34] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-78] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [50-70] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-109] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-122] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-149] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-129] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-142] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-104] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [112-124] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [126-130] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-137] for track '24' has 1 frames without a visible bounding box.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.