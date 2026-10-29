# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Duo_9`
- **Input XML**: `outputs/batch/Duo/Duo/Duo_9/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Duo.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 81 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [0-187] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-143] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [145-146] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-187] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-157] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [113-158] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [183-193] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [91-122] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [131-138] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-86] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-106] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [111-114] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [121-131] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [135-194] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-198] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-202] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-207] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-149] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [155-166] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-187] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-187] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [193-209] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-195] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-133] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 152, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [152-152] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-130] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' for track '17' starts at frame 91, but the player has no visible bounding box on this frame.
> - Action 'Action_ComboBlock' range [91-91] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [103-107] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [111-139] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-184] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-114] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [116-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-132] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [136-143] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [149-170] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-209] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-154] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_ComboBlock' range [91-151] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-209] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-18] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [20-21] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [24-26] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [29-40] for track '22' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [44-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [66-69] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [71-72] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-144] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [147-163] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [169-172] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [159-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-171] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-193] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [166-172] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [180-203] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [205-209] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-197] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-209] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-208] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [190-209] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [198-201] for track '36' has 1 frames without a visible bounding box.
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