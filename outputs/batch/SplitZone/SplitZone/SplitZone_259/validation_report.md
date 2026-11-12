# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_259`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_259/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 102 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '13' (LT) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
> - Validation warning: Action 'Action_ZoneBlock' for track '15' (C) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [112–127], lower_priority='Action_ZoneBlock' annotated_start=115, effective_Action_ZoneBlock_start=128.
> - Validation warning: Action 'Action_ZoneBlock' for track '18' (RG) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (RT) duration 96 frames exceeds threshold 90 frames [start=115, end=210].
> - Action 'Action_None' range [112-290] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [292-389] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [112-315] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-319] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-372] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [374-376] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [381-382] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-161] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-167] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-216] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-389] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-368] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-389] for track '8' has 4 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [122-194] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-389] for track '9' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [112-165] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-149] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [140-372] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [128-131] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [151-179] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-389] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-220] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-232] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-236] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-244] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-204] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-389] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [115-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-296] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-316] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-389] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-389] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [215-218] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-260] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-366] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-275] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [278-280] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [286-292] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [295-311] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-317] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [352-358] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [327-328] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [331-334] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-345] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-350] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [348-352] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [358-361] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [364-365] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [377-378] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [375-378] for track '35' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.