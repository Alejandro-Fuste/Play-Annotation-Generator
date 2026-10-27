# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_322`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_322/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 646: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [47–63], lower_priority='Action_DownBlock' annotated_start=50, effective_Action_DownBlock_start=64.
> - Action 'Action_None' range [47-118] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-53] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [90-233] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [237-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-124] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-82] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-130] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-108] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-100] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-113] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-130] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-178] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-55] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-95] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-130] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [50-118] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [50-73] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [78-79] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [82-130] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-222] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [64-73] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [77-98] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [131-197] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-66] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-110] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [112-119] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-202] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-56] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-65] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [37-41] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-46] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 47, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [47-47] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-56] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-83] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-104] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-128] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-225] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-141] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-141] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-160] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-186] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-193] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-229] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [217-219] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-239] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-227] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-239] for track '32' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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