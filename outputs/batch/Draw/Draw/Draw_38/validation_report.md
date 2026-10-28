# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_38`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_38/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 110 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '9' (C): higher_priority='Action_BallSnap' [56–74], lower_priority='Action_PassBlock' annotated_start=59, effective_Action_PassBlock_start=75.
> - Action 'Action_None' range [56-91] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-123] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-299] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [101-135] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-162] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-174] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-189] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-103] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-116] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-74] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-154] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [119-138] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [160-211] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-116] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-120] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-181] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-236] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-271] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-292] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-30] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [56-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [63-70] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-78] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-83] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [59-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_SnapReceive' range [56-67] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-230] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-42] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-84] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-299] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-72] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-162] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-94] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [101-141] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-157] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-108] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [94-125] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-122] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-228] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-290] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-184] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-229] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-265] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-273] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-217] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-251] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-193] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-177] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-204] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-238] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-235] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-252] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-241] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-267] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-278] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-279] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [281-287] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-256] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-289] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-290] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [276-285] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-289] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [295-299] for track '34' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.