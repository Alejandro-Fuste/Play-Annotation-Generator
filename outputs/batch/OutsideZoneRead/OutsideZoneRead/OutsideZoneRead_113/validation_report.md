# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneRead_113`
- **Input XML**: `outputs/batch/OutsideZoneRead/OutsideZoneRead/OutsideZoneRead_113/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneRead.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 24 |
| Action Segments inferred | 89 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_ZoneBlock' annotated_start=27, effective_Action_ZoneBlock_start=39.
> - Action 'Action_None' range [24-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-188] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-223] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-129] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [24-97] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-239] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-51] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [54-55] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-212] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [24-103] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [24-35] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [39-43] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [64-102] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [58-61] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [72-170] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [176-187] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [189-212] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [214-217] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-71] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-66] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [70-73] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-87] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-239] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-49] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [55-60] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [62-64] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-104] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [24-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [27-44] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-126] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [53-54] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-70] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-161] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-155] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-218] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-224] for track '30' has 1 frames without a visible bounding box.
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