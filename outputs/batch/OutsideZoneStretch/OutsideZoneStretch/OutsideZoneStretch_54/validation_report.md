# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutsideZoneStretch_54`
- **Input XML**: `outputs/batch/OutsideZoneStretch/OutsideZoneStretch/OutsideZoneStretch_54/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutsideZoneStretch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 16 |
| Action Segments inferred | 106 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Action 'Action_PreSnap' range [0-329] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [217-218] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [223-309] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-329] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-214] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-329] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-227] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [241-298] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [310-311] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-219] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [153-204] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-221] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-169] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-165] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [168-329] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-199] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [202-203] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-208] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [211-230] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-277] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [280-329] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-293] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-301] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-166] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [174-181] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [183-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-234] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [236-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-252] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-158] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-160] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [11-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-30] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [56-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [107-111] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [124-152] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [154-232] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [176-186] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-193] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [186-233] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [188-221] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [227-329] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [192-199] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [201-204] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [209-217] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-229] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [258-262] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [270-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [277-286] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [290-291] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [293-295] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [300-306] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [311-313] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [316-319] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [322-325] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [197-199] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [230-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [200-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [206-209] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-234] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [242-245] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [259-260] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [207-209] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [212-214] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [219-230] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [220-221] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [243-244] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [249-293] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [295-303] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [305-329] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [229-230] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [239-329] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [255-283] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [298-301] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [303-305] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [307-329] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [261-262] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [271-272] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [275-278] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [296-308] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [297-298] for track '38' has 1 frames without a visible bounding box.
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
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.