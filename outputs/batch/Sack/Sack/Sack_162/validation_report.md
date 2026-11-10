# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Sack_162`
- **Input XML**: `outputs/batch/Sack/Sack/Sack_162/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Sack.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 13 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 326: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [132-136] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [93-94] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [96-106] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_CloseOnQuarterback' range [108-110] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-56] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-92] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [94-112] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-123] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-140] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-110] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [113-114] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [120-125] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_WrapQuarterback' range [127-140] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-46] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-68] for track '13' has 5 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-83] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-114] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [123-124] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-139] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-144] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-53] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-92] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-103] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-110] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-15] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-44] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [57-116] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_SackQuarterback' range [141-146] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-16] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-46] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-59] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-9] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-11] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-44] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-92] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [96-110] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-41] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-9] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-15] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-55] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-63] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [67-78] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [80-115] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-131] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [146-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-80] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-121] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [129-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [134-142] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-110] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [120-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [127-130] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [95-110] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [113-114] for track '24' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '4' has undefined position. Will map to Position_Unknown.
> - Player track '4' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.