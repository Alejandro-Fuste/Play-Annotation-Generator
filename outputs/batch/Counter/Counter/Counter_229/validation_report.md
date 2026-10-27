# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_229`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_229/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 31 |
| Player Tracks | 31 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 118 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 460: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '9' (RT) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
> - Validation warning: Action 'Action_DownBlock' for track '14' (DE2) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
> - Validation warning: Action 'Action_DownBlock' for track '20' (RG) duration 134 frames exceeds threshold 90 frames [start=113, end=246].
> - Action 'Action_None' range [111-196] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-158] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-167] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-359] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-359] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-359] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-239] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-290] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-178] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-340] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [343-355] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [111-238] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-249] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-261] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-330] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-149] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-203] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-324] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [332-333] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-122] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-303] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [308-311] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-319] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-146] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-154] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-211] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-204] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-359] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [113-140] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [145-153] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-160] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [177-211] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [113-199] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-108] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-132] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-162] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [171-222] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-269] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-310] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-323] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-358] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-184] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-190] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-359] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-301] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-359] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [338-340] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-271] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [328-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-333] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [349-350] for track '30' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.