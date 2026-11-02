# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_93`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_93/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 49 |
| Player Tracks | 46 |
| Ball Tracks | 3 |
| CSV events parsed | 21 |
| Action Segments inferred | 96 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Resolved action overlap for track '8' (C): higher_priority='Action_BallSnap' [61–72], lower_priority='Action_ZoneBlock' annotated_start=62, effective_Action_ZoneBlock_start=73.
> - Action 'Action_None' range [61-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SealBlock' range [62-99] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-87] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-157] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-94] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-102] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-107] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-90] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [73-86] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [88-94] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-359] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-91] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-99] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-72] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [61-95] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-61] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '13' starts at frame 103, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [103-103] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-3] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-44] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-84] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_JetMotion' range [69-88] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [89-111] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [71-265] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [268-305] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-74] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-104] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-102] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-105] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [90-102] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-124] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-105] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [85-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-121] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-99] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-107] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-103] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-136] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-310] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-119] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [133-211] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-268] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [305-359] for track '32' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [136-259] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-290] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-334] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-359] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-225] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-230] for track '39' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [279-285] for track '40' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-329] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [334-340] for track '41' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [342-347] for track '41' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [317-327] for track '44' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [321-326] for track '45' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-344] for track '47' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-354] for track '48' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '9' has undefined position. Will map to Position_Unknown.
> - Player track '9' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '44' has undefined position. Will map to Position_Unknown.
> - Player track '44' has undefined team_side. Will map to Team_Unknown.
> - Player track '45' has undefined position. Will map to Position_Unknown.
> - Player track '45' has undefined team_side. Will map to Team_Unknown.
> - Player track '47' has undefined position. Will map to Position_Unknown.
> - Player track '47' has undefined team_side. Will map to Team_Unknown.
> - Player track '48' has undefined position. Will map to Position_Unknown.
> - Player track '48' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.