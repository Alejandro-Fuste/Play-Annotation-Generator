# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_167`
- **Input XML**: `outputs/batch/Power/Power/Power_167/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 33 |
| Player Tracks | 33 |
| Ball Tracks | 0 |
| CSV events parsed | 14 |
| Action Segments inferred | 80 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 359 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 336: Duplicate assignment for track ID '6' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 359 as fallback play end.
> - Action 'Action_PreSnap' range [22-234] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [247-285] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-296] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [318-320] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [323-333] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-298] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-242] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [284-285] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-359] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-232] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-241] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-267] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-288] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-140] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [142-143] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-323] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-345] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-300] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-352] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-359] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-277] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-281] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-304] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [306-346] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [348-354] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-266] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [275-279] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-277] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [218-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [239-253] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [255-277] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [285-287] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-222] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [263-284] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-230] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-257] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [260-276] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [278-279] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-322] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-78] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [218-243] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [245-259] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [87-292] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-308] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-315] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-340] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-232] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-301] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-315] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [317-354] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-315] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [312-315] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [313-314] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-359] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [328-329] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [330-359] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [334-345] for track '31' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [349-350] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [352-353] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-358] for track '31' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.