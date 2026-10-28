# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_13`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_13/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 177 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [51–64], lower_priority='Action_PassBlock' annotated_start=54, effective_Action_PassBlock_start=65.
> - Action 'Action_None' range [51-128] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-170] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [173-228] for track '0' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [232-273] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-121] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-92] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [99-101] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-203] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-200] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-209] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-251] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-154] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-195] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-211] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [213-227] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-133] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-169] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-199] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-223] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [247-248] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-287] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-121] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-151] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-262] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-126] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [51-270] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-291] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [294-295] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-77] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [80-81] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-108] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-148] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-169] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-298] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-99] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-299] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [99-120] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-133] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-169] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [225-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-164] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-295] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-85] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [112-117] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [121-123] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [129-134] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [139-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [150-151] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-250] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-263] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-106] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-121] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-169] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-193] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-231] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-246] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-255] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-263] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-284] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [288-299] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-8] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-29] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-114] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-239] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-269] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-202] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-173] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-181] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-198] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-184] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-299] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-251] for track '32' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [254-280] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [285-287] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-291] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-214] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-260] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-203] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-247] for track '34' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-239] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-258] for track '35' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [262-271] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-287] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-298] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-239] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-250] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-258] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-287] for track '36' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [235-237] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-257] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-239] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-250] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [293-294] for track '43' has 1 frames without a visible bounding box.
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
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.