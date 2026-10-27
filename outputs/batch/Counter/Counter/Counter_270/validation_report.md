# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_270`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_270/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 105 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Segment 'Action_BallCarry' for track '6' has invalid range: start=187, end=180. Clamping end to start.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [144–158], lower_priority='Action_PullBlock' annotated_start=147, effective_Action_PullBlock_start=159.
> - Action 'Action_None' range [144-226] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [259-337] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [344-345] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-359] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-286] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-293] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [297-304] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-185] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-216] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-359] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_Handoff' range [168-175] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-256] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-314] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-180] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [147-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-191] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-288] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [159-164] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [167-171] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [176-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [179-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-319] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-203] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-253] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-193] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-318] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-149] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [155-188] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [190-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-234] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-281] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-209] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-339] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-235] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-282] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-249] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-252] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-338] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [343-351] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-276] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [310-344] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-351] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-301] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-305] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [272-278] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-288] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-295] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [287-359] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-359] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [292-323] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [330-343] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [346-359] for track '31' has 1 frames without a visible bounding box.
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
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.