# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: FAILED
- **Video Name**: `CrackToss_53`
- **Input XML**: `outputs/batch/CrackToss/CrackToss/CrackToss_53/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/CrackToss.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 17 |
| Action Segments inferred | 83 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
> [!CAUTION]
> The following critical issues were encountered:
> - Event 'Action_None' at frame 117 targets track ID '146', but it is not found in XML.

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 107: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 108: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Track ID '0' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '17' (Unknown) duration 114 frames exceeds threshold 90 frames [start=62, end=175].
> - Validation warning: Action 'Action_PullBlock' for track '18' (TE) duration 114 frames exceeds threshold 90 frames [start=62, end=175].
> - Action 'Action_None' range [59-140] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-160] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-168] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-148] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-157] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-172] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-175] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-119] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [124-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-158] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-175] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-175] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-86] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [91-151] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-125] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-148] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-175] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [59-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-107] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-175] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [62-145] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [148-152] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_CrackBlock' range [158-175] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-113] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [116-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [62-107] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [110-175] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-121] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-163] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-100] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-137] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [139-175] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [59-147] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-175] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-175] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-149] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-153] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-158] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-150] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-159] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-166] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-175] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-175] for track '29' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Fix the missing/invalid track IDs in the action CSV so they match the XML track structure.
- Resolve the overlapping action segment ranges noted above by adjusting the start frames in the CSV.
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.