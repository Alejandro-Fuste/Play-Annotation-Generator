# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `RPO_90`
- **Input XML**: `outputs/batch/RPO/RPO/RPO_90/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/RPO.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 34 |
| Player Tracks | 34 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Action 'Action_None' range [63-269] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-226] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-262] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-229] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-237] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [239-242] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-269] for track '2' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [63-228] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-246] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [250-265] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-189] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-191] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [193-234] for track '6' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [257-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-222] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-219] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-108] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-112] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [115-120] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [135-255] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-84] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [92-113] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-252] for track '11' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [255-265] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-199] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [201-234] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [252-253] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [257-260] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-227] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-255] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-245] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-238] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-242] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-143] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [151-157] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [64-116] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [122-123] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' for track '20' starts at frame 64, but the player has no visible bounding box on this frame.
> - Action 'Action_ZoneBlock' range [64-64] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [68-70] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [72-74] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [80-82] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-144] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-204] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-85] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-117] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-126] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-182] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-167] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-212] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-229] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-233] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-250] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-261] for track '32' has 1 frames without a visible bounding box.
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