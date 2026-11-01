# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `InsideZoneRead_261`
- **Input XML**: `outputs/batch/InsideZoneRead/InsideZoneRead/InsideZoneRead_261/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/InsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_ZoneBlock' for track '18' has invalid range: start=13, end=9. Clamping end to start.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_ZoneBlock' annotated_start=13, effective_Action_ZoneBlock_start=25.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [10–24], lower_priority='Action_SnapReceive' annotated_start=10, effective_Action_SnapReceive_start=25.
> - Action 'Action_None' range [10-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-61] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-66] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-150] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [153-197] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '3' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [10-43] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-206] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-58] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-82] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-36] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-120] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-192] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [10-115] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-142] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-189] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-87] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [78-207] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [10-115] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-119] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-40] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [44-77] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-202] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-184] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-209] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-210] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ReadDefender' range [32-38] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [39-57] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [58-59] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [10-129] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-210] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-31] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [34-36] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [13-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-210] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-43] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-50] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-59] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-196] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-89] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-202] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-100] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-191] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-124] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-119] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-122] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-131] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-157] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-186] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-157] for track '30' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [160-170] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '30' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [134-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-197] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '33' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.