# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_231`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_231/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '4' (C): higher_priority='Action_BallSnap' [82–94], lower_priority='Action_ZoneBlock' annotated_start=85, effective_Action_ZoneBlock_start=95.
> - Action 'Action_ZoneBlock' range [95-98] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [107-109] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [111-128] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [150-181] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-112] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-138] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-145] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_Handoff' for track '9' starts at frame 109, but the player has no visible bounding box on this frame.
> - Action 'Action_Handoff' range [109-109] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-193] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [199-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-228] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [231-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-227] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-201] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-239] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-211] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [82-116] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-219] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-120] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-131] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [133-138] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [85-118] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-134] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-148] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-164] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-187] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-228] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-200] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-220] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-217] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-229] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-233] for track '31' has 1 frames without a visible bounding box.
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