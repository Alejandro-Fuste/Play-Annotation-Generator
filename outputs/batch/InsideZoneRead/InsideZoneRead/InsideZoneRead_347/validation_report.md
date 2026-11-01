# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_347`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_347/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '5' has invalid range: start=59, end=40. Clamping end to start.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [13–27], lower_priority='Action_ZoneBlock' annotated_start=16, effective_Action_ZoneBlock_start=28.
> - Action 'Action_None' range [13-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-38] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-164] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-177] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-188] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_Keep' range [38-40] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-91] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-113] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-84] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-69] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-210] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-115] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-138] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [13-209] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-42] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-152] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-206] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [13-209] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-112] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-210] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [13-210] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [28-29] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-82] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-113] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-121] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-134] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [38-48] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [55-81] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 90, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [90-92] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-38] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [16-56] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-210] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-60] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-67] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-70] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-80] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-97] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-116] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-127] for track '24' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [130-134] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-145] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [65-116] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [118-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-210] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [126-210] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-154] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-169] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-180] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-188] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-180] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-192] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-192] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '34' has 1 frames without a visible bounding box.
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