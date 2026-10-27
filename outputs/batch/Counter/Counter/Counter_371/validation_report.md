# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_371`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_371/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 158 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Validation warning: Action 'Action_PullBlock' for track '15' (C) duration 93 frames exceeds threshold 90 frames [start=35, end=127].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [32–46], lower_priority='Action_PullBlock' annotated_start=35, effective_Action_PullBlock_start=47.
> - Validation warning: Action 'Action_DownBlock' for track '21' (LT) duration 93 frames exceeds threshold 90 frames [start=35, end=127].
> - Action 'Action_None' range [32-359] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [35-81] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-333] for track '2' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [32-73] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-95] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-321] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-328] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-217] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-245] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-254] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-359] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-142] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-288] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-288] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [294-296] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-139] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-174] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-334] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [347-357] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-356] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [32-109] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-173] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [73-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [104-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [108-124] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [126-141] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [144-187] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [190-191] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [202-205] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [208-224] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [229-233] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [236-238] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [245-247] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [298-301] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [306-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [47-71] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-318] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [340-352] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-262] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [282-283] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-303] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [306-311] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [328-331] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-335] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [339-344] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-114] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-124] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-152] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-178] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-232] for track '17' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [235-242] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-249] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-262] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-305] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [308-315] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-318] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-321] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-333] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [32-258] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [260-296] for track '19' has 6 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [35-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [42-54] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [35-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [55-56] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [105-125] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-170] for track '22' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-125] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-189] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-211] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-222] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-240] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-250] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-264] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-314] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-326] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [329-337] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [76-84] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-93] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-124] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-185] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-211] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-219] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-241] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-275] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-173] for track '26' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-358] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-174] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [188-189] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-247] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-254] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-262] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-272] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-288] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-326] for track '30' has 2 frames without a visible bounding box.
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