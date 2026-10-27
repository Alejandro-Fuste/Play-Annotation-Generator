# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_4`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 10: Duplicate assignment for track ID '10' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [80-121] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [91-103] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [133-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [152-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [159-172] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [91-114] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [125-172] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-181] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-279] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-236] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-125] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [153-157] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-112] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-143] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-195] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-143] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-57] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [81-92] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-117] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-295] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-110] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-174] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-214] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-42] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-111] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-129] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-152] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-201] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-92] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-104] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-181] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-93] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-109] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-150] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [76-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [109-124] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-167] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-17] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [61-62] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-68] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [74-79] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [82-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-244] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-185] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-261] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-207] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-281] for track '23' has 2 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.