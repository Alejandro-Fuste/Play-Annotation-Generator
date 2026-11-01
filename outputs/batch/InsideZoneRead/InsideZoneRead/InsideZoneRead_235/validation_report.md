# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_235`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_235/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 101 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '19' (C): higher_priority='Action_BallSnap' [91–105], lower_priority='Action_ZoneBlock' annotated_start=94, effective_Action_ZoneBlock_start=106.
> - Action 'Action_None' range [91-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-242] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-260] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-165] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-256] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-149] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-226] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [228-229] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-244] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-252] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-254] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-252] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-22] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-121] for track '15' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-141] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [134-138] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [141-142] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [146-153] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-103] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [125-126] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-135] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-112] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [119-120] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '19' starts at frame 106, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [106-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [94-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-170] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-178] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-90] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [112-113] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-180] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-242] for track '21' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-10] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [129-131] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-199] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-183] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-195] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-212] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [219-222] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [224-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-250] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-244] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-258] for track '33' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-269] for track '35' has 1 frames without a visible bounding box.
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