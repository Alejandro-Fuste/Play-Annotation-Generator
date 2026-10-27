# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_285`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_285/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 19 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 571: Duplicate assignment for track ID '18' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '13' (RT) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
> - Validation warning: Action 'Action_PullBlock' for track '17' (LG) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
> - Validation warning: Action 'Action_DownBlock' for track '20' (C) duration 97 frames exceeds threshold 90 frames [start=144, end=240].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [141–157], lower_priority='Action_DownBlock' annotated_start=144, effective_Action_DownBlock_start=158.
> - Action 'Action_None' range [141-385] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-250] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-178] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-304] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-324] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-337] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-352] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-362] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-195] for track '11' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-85] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-183] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-293] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [144-173] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [177-186] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [188-240] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-286] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-350] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [352-353] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-358] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-267] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [277-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-313] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-380] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-355] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [188-374] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [144-240] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-279] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [144-216] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-389] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [158-163] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-273] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-389] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-230] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-252] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-23] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [28-33] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-37] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-218] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-239] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-299] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-290] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-320] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-342] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-355] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [314-320] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [350-365] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [367-368] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [357-389] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [361-385] for track '31' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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