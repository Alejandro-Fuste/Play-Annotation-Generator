# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_112`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_112/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Action 'Action_PreSnap' range [0-89] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-289] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-182] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-294] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-201] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [196-212] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_Keep' range [217-360] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_Keep' range [363-364] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [221-224] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [226-227] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [237-245] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-182] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [184-214] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-233] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-246] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-197] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-250] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-170] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-179] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [10-364] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-196] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-367] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-10] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-220] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [221-222] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-235] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-276] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [185-200] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-232] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-247] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [252-363] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [365-389] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [191-194] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-212] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [214-389] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [224-238] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-268] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [262-263] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [265-350] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [356-357] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [360-361] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [335-336] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [351-358] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [369-373] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [359-368] for track '32' has 3 frames without a visible bounding box.
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