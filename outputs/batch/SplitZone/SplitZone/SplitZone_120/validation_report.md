# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_120`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_120/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 30 |
| Player Tracks | 30 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 94 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [145–158], lower_priority='Action_ZoneBlock' annotated_start=148, effective_Action_ZoneBlock_start=159.
> - Action 'Action_None' range [145-201] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-213] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [215-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-265] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-241] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-304] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [306-308] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [315-316] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-303] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-178] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [185-221] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [148-221] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-251] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [254-308] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [178-251] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [254-259] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [262-291] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [145-187] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-206] for track '7' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [254-256] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-297] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-224] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-271] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-277] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [145-207] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-233] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [145-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [159-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [177-190] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [212-216] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-224] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-304] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [307-308] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-23] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [26-46] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-54] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-65] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [69-72] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-191] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-197] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-304] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-283] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-323] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-273] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-297] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-314] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [322-325] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-310] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [312-316] for track '29' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.