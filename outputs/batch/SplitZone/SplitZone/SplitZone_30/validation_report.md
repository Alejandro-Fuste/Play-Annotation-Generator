# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_30`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_30/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Track ID '14' in Player Track ID sheet does not exist in MOT gt.txt.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [115–130], lower_priority='Action_ZoneBlock' annotated_start=118, effective_Action_ZoneBlock_start=131.
> - Action 'Action_None' range [115-165] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' for track '3' starts at frame 160, but the player has no visible bounding box on this frame.
> - Action 'Action_BallCarry' range [160-160] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [162-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [180-222] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [225-226] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-203] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-225] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-264] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-242] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-151] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-264] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [152-158] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-140] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-182] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [118-170] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [131-148] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [150-166] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-122] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-134] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-154] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-193] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-198] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [18-35] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-72] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-114] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '14' starts at frame 115, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [115-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-184] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-189] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-269] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-218] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [247-267] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-241] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [262-264] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-226] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-249] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-269] for track '27' has 1 frames without a visible bounding box.
> - Player track '11' has undefined position. Will map to Position_Unknown.
> - Player track '11' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.