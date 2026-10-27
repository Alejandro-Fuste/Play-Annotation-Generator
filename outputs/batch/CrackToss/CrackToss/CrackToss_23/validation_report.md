# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `CrackToss_23`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_23/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 26 |
| Player Tracks | 26 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 328 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 48: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 48: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 328 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '19' (LG) duration 117 frames exceeds threshold 90 frames [start=83, end=199].
> - Action 'Action_None' range [80-168] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-172] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-191] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-267] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-282] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [80-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-141] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-328] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-156] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-183] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-149] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-263] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-311] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [120-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-25] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [27-28] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-168] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-135] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-328] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-161] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-296] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [80-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-149] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-328] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [23-24] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [58-68] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [70-79] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [83-196] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [8-13] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-149] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-254] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-5] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-17] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-79] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '21' starts at frame 80, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [80-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-148] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-328] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-206] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-328] for track '24' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.