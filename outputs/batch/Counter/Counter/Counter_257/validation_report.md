# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_257`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_257/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [75–79], lower_priority='Action_DownBlock' annotated_start=78, effective_Action_DownBlock_start=80.
> - Action 'Action_PreSnap' range [0-27] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-38] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-122] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-141] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-151] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [136-140] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-232] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-149] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [78-146] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-159] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-126] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-143] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-160] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-181] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-196] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-299] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-161] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-299] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-156] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [75-160] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-173] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [80-139] for track '11' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [142-143] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-79] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-117] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-242] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-289] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-77] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [78-106] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [109-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-74] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-107] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-28] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [30-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-98] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-26] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [34-41] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-50] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '18' starts at frame 80, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [80-80] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' range [104-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-272] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [88-94] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [100-122] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [124-146] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [147-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-11] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-69] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-129] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-272] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [3-10] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [89-128] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [130-144] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-267] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-112] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-127] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-160] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [111-117] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-177] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-152] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-253] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-190] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-180] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [192-299] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [238-270] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-262] for track '31' has 1 frames without a visible bounding box.
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