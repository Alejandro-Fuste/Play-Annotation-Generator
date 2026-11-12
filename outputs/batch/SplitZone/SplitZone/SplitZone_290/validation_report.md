# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_290`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_290/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 121 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [43–55], lower_priority='Action_ZoneBlock' annotated_start=54, effective_Action_ZoneBlock_start=56.
> - Action 'Action_None' range [43-143] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-149] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-198] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-82] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-90] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-309] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [315-330] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-359] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-135] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [141-142] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [79-85] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-163] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-189] for track '8' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-299] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [52-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [86-128] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-74] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [82-86] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [90-93] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-120] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-189] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-359] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '16' starts at frame 113, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [113-113] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-177] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [179-200] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-217] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-253] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-91] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [94-99] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-204] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [56-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-139] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-159] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-171] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-52] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-63] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-88] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-114] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-188] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-88] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-215] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-153] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-167] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [169-196] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [129-133] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-334] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [338-359] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-163] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-183] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-211] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-225] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [160-190] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-187] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-168] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-186] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-219] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [269-270] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-281] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-359] for track '38' has 2 frames without a visible bounding box.
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