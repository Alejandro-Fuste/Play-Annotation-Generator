# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_181`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_181/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 364: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 364: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '19' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
> - Validation warning: Action 'Action_DownBlock' for track '20' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
> - Validation warning: Action 'Action_PullBlock' for track '21' (Unknown) duration 92 frames exceeds threshold 90 frames [start=186, end=277].
> - Action 'Action_None' range [183-257] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-264] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-289] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-306] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-385] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-359] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [362-363] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-369] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-307] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-327] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-376] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [378-383] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-280] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-291] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-389] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-207] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-338] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [204-359] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [186-251] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [255-256] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [263-264] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '12' starts at frame 278, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [278-278] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-326] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-332] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-197] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [209-211] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [233-238] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [242-243] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-222] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [204-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-361] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [186-202] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-223] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-307] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [309-311] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-329] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-386] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-343] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-351] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-356] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-383] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [385-386] for track '32' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
> - Player track '3' has undefined position. Will map to Position_Unknown.
> - Player track '3' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.