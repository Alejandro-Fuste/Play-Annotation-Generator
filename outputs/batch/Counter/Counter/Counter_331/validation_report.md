# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_331`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_331/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 43 |
| Player Tracks | 43 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 138 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 663: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - Row 664: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [133–146], lower_priority='Action_DownBlock' annotated_start=136, effective_Action_DownBlock_start=147.
> - Action 'Action_None' range [133-274] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [136-182] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [189-191] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-283] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-168] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-250] for track '5' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [261-301] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-273] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-329] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-152] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-173] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-251] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-177] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [206-212] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-219] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-188] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-209] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-224] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-316] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [322-323] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-268] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-294] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-301] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-313] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [136-222] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-265] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [136-172] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [188-189] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-329] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-9] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [16-25] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-30] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [33-83] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [15-45] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-62] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-164] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-177] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-195] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-313] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [321-322] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [324-325] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-243] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-185] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-206] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-326] for track '28' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-203] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [202-209] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-272] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-250] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-255] for track '36' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-329] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-277] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-296] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-311] for track '38' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-326] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-274] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [288-289] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-304] for track '39' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [284-287] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-301] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [288-293] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-301] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [296-301] for track '42' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '42' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [311-319] for track '42' has 1 frames without a visible bounding box.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.