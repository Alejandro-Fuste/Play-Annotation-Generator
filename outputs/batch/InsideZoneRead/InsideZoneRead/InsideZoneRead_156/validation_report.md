# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_156`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_156/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 93 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '12' (RT) duration 93 frames exceeds threshold 90 frames [start=108, end=200].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [105–120], lower_priority='Action_ZoneBlock' annotated_start=108, effective_Action_ZoneBlock_start=121.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 93 frames exceeds threshold 90 frames [start=108, end=200].
> - Action 'Action_None' range [105-148] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-241] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-229] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-248] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-269] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-243] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-253] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [108-143] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-269] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [150-214] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [240-269] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-122] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-127] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-201] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-172] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-245] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [253-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-244] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-245] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-53] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '21' starts at frame 108, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [108-108] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-119] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-141] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [49-73] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-128] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [143-147] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-185] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-252] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-169] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-177] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-189] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-251] for track '30' has 1 frames without a visible bounding box.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.