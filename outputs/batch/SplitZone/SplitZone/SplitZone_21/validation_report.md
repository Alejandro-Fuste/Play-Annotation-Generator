# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_21`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_21/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 449 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 449 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [79–95], lower_priority='Action_ZoneBlock' annotated_start=82, effective_Action_ZoneBlock_start=96.
> - Action 'Action_None' range [79-258] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-300] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [304-449] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [84-85] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [89-113] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [121-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-167] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-226] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-114] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-449] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-203] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-64] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-80] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-329] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-118] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-156] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-174] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-258] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-294] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [296-298] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-59] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-354] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [356-419] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-32] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-58] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-294] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-58] for track '13' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [89-92] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-111] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-51] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-113] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [116-117] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-138] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-336] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-119] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [120-137] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [79-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [88-93] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [161-291] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-309] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-63] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-77] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-160] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-193] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-258] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-63] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [75-76] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-112] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [121-156] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-225] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-289] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-28] for track '20' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-41] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [95-96] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [5-29] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-50] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-58] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [110-114] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-198] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-215] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [226-261] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [109-115] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-298] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-449] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-156] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-170] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-176] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-202] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-281] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-135] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-242] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [138-140] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-171] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-285] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-160] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-173] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-332] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-270] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [316-318] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [325-345] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-339] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [336-337] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [365-366] for track '35' has 1 frames without a visible bounding box.
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